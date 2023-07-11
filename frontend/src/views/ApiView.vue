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
      <div v-for="image in responseImages" :key="image.id">
        <img :src="image.url" :alt="image.id" />
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
      // Obtener el archivo de imagen
      const file = this.uploadedImage;

      // Crear un objeto FormData para enviar el archivo
      const formData = new FormData();
      formData.append('file', file);
      formData.append('k', this.k)

      this.loading = true;

      // Realizar la llamada a la API
      fetch(`/api/upload-image`, {
          method: 'POST',
          body: formData
      })
      .then(response => response.json())
      .then(data => {
        // Actualizar this.responseImages con las imágenes devueltas por la API
        this.responseImages = data.images;
        this.loading = false;
      })
      .catch(error => {
        console.error(error);
        this.loading = false;
      });

      // simulación de respuesta de la API
      this.responseImages = [
        { id: 1, url: "../images/A.jpg" },
        { id: 2, url: "../images/P.jpg" },
        { id: 3, url: "../images/Y.jpg" }
      ];
    }
  }
};
</script>