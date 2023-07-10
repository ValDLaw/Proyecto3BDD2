<template>
    <div class="container">
      <input type="file" @change="handleFileUpload" accept="image/*" />
      <label for="k">Valor k:</label>
      <input type="number" id="k" v-model="k" />
      <div v-if="uploadedImage">
        <h2>Imagen cargada:</h2>
        <br>
        <div class="image-container">
          <img :src="uploadedImage" alt="Imagen cargada" class="uploaded-image" />
        </div>
        <button @click="submitImage">Enviar imagen</button>
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
        uploadedImage: '',
        responseImages: [],
        k: 0
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

        // Realizar la llamada a la API
        fetch(`/api/upload-image`, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
        // Actualizar this.responseImages con las imágenes devueltas por la API
        this.responseImages = data.images;
        })
        .catch(error => {
        console.error(error);
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
  
  <style>
  .container {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
  }
  
  .image-container {
    height: 300px;
    overflow: hidden;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
  }
  
  .uploaded-image {
    height: 100%;
  }
  </style>
  