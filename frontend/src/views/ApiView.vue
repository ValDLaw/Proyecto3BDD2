<template>
  <div class="container">

    <div v-if="loading" class="loading-screen">
      <div class="loader"></div>
      <p>Cargando...</p>
    </div>  

    <div class="input-container">
      <label for="k">Valor k:</label>
      <div class="custom-input">
        <input type="number" id="k" min="1" v-model="k" />
      </div>
    </div>
    
    <input id="fileInput" type="file" @change="handleFileUpload" accept="image/*" />
    <label for="fileInput" class="custom-file-button">Subir foto</label>
    
    <div class="container" v-if="uploadedImage">
      <div class="image-container">
        <img :src="uploadedImage" alt="Imagen cargada" class="uploaded-image" />
      </div>
      <button @click="submitImage" class="custom-file-button">¡Descúbre tu doppelgänger!</button>
    </div>

    <div v-if="responseImages.length > 0">
      <h2>Imágenes obtenidas:</h2>
      <div class="image-container">
        <!-- Muestra la primera imagen de forma especial -->
        <div class="original-image-container">
          <h3>Este es tu doppelgänger famoso!</h3>
          <img :src="responseImages[0].url" :alt="responseImages[0].id" class="original-image" />
        </div>
        <p>Para ver más resultados, puedes mirar abajo.</p>
      </div>
      <div class="result-images-container">
        <div v-for="(image, index) in responseImages.slice(1)" :key="image.id" class="result-image">
          <h4>{{ index + 1 }}</h4>
          <img :src="image.url" :alt="image.id" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
      uploadedImage: '',
      responseImages: [],
      k: 3
    };
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.uploadedImage = reader.result;
      };

      reader.readAsDataURL(file);
    },
    
    submitImage() {
      this.loading = true; // Mostrar el indicador de carga

      const formData = new FormData();
      formData.append('file', this.dataURLtoFile(this.uploadedImage, 'image.jpg')); // Convierte la imagen a un archivo
      formData.append('k', this.k);

      fetch('http://127.0.0.1:5000/sequential', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        // Actualiza los resultados obtenidos
        this.responseImages = data.map((path, index) => {
          return {
            id: index + 1,
            url: path.substring(2)
          };
        })
        this.loading = false; // Oculta el indicador de carga
        console.log('Success:', this.responseImages);
      })
      .catch(error => {
        console.error('Error:', error);
        this.loading = false; // Oculta el indicador de carga en caso de error
      });
    },

    dataURLtoFile(dataURL, filename) {
      const arr = dataURL.split(',');
      const mime = arr[0].match(/:(.*?);/)[1];
      const bstr = atob(arr[1]);
      let n = bstr.length;
      const u8arr = new Uint8Array(n);
      while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
      }
      return new File([u8arr], filename, { type: mime });
    }
  }
};
</script>
