<template>
  <div id="app">
    <header>
      <title>Encuentra tu doppelgänger</title>
      <div class="containerA">
        <h1 style="font-size: 3em;" class="animated-title">¡Encuentra tu doppelgänger!</h1>
      </div>
      <nav>
        <ul class="nav-list">
          <li :class="{ active: $route.name === 'SequentialView' }"><router-link :to="{ name: 'SequentialView' }">Sequential</router-link></li>
          <li :class="{ active: $route.name === 'FaissView' }"><router-link :to="{ name: 'FaissView' }">Faiss</router-link></li>
          <li :class="{ active: $route.name === 'RTreeView' }"><router-link :to="{ name: 'RTreeView' }">R-Tree</router-link></li>
          <li :class="{ active: $route.name === 'KDTreeView' }"><router-link :to="{ name: 'KDTreeView' }">KD-Tree</router-link></li>
        </ul>
      </nav>
    </header>
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Caprasimo&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Avenir:ital,wght@0,400;0,500&display=swap');

/* Global styles */
:root {
  --primary-color: #014c75;
  --secondary-color: #ccdde6;
  --accent-color: #014c75;
  --background-color: #fff7f1;
}

body {
  margin: 0;
  font-family: 'Avenir', sans-serif;
  background-color: var(--background-color);
  color: var(--primary-color);
}

.containerA {
  display: flex;
  justify-content: center;
  align-items: center;
  height: auto;
}

/* Navigation styles */
nav {
  background-color: var(--secondary-color);
  padding: 10px;
}

.nav-list {
  list-style: none;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
}

.nav-list li {
  margin-right: 10px;
}

.nav-list li:last-child {
  margin-right: 0;
}

.nav-list li a {
  text-decoration: none;
  color: var(--primary-color);
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-list li.active a {
  background-color: var(--accent-color);
  color: var(--secondary-color);
  /* Additional styles to highlight the active button */
}

.nav-list li a:hover {
  background-color: var(--accent-color);
  color: var(--secondary-color);
}

/* Other styles */
h1 {
  font-family: 'Caprasimo', sans-serif;
  font-weight: normal;
  color: var(--primary-color);
}
h2 {
  font-family: 'Avenir', sans-serif;
  font-weight: 600; /* Slightly bolder headings */
  color: var(--primary-color);
}

h3, h4, h5, h6 {
  font-family: 'Avenir', sans-serif;
  font-weight: 500;
  color: var(--primary-color);
}

.container {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  margin: 20px;
}

.container input[type="file"] {
  display: none;
}

.custom-file-button {
  margin:20px;
  background-color: var(--secondary-color);
  color: var(--accent-color); /* Use accent color for button text */
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-family: 'Avenir', sans-serif;
  font-weight: 500;
  transition: background-color 0.3s;
}

.custom-file-button:hover {
  background-color: var(--accent-color);
  color: var(--secondary-color); /* Use secondary color for button text on hover */
}

.input-container {
  display: flex;
  align-items: center;
}

.input-container label {
  font-weight: bold;
  margin-right: 10px;
}

.custom-input {
  position: relative;
  width: 80px;
}

.custom-input input[type="number"] {
  width: 100%;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-family: 'Avenir', sans-serif;
}

.custom-input::before {
  content: "";
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  width: 7px;
  height: 7px;
  border-top: 1px solid #ccc;
  border-right: 1px solid #ccc;
  transition: transform 0.2s;
  pointer-events: none;
}

.custom-input input[type="number"]:focus + ::before {
  transform: translateY(-50%) rotate(45deg);
}

.image-container {
  width: 80%;
  display: grid;
  grid-template-columns: 1fr 1fr; /* Dos columnas de igual tamaño */
  column-gap: 20px; /* Espacio entre las columnas */
  margin: 15px;
}

.uploaded-image-container,
.response-image-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.response-image-wrapper,
.uploaded-image-wrapper {
  height: 200px; /* Altura fija */
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0; /* Inicialmente oculto */
  animation: imageAppear 0.5s ease-in-out forwards; /* Animación de aparición */
}

@keyframes imageAppear {
  0% {
    opacity: 0;
    transform: translateY(-20px); /* Desplazamiento hacia arriba */
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.response-image-container h3 {
  margin-top: 0;
}

.response-image {
  height: 100%;
}

.uploaded-image {
  width: 70%;
}

.result-images-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.result-image {
  flex-basis: 20%;
  text-align: center;
  margin: 15px;
}

.loading-screen {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5); /* Fondo semitransparente */
  z-index: 9999; /* Asegura que la pantalla de carga se superponga a otros elementos */
}

.loader {
  border: 4px solid #f3f3f3; /* Color del borde del loader */
  border-top: 4px solid var(--accent-color); /* Color del borde superior del loader */
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite; /* Animación giratoria */
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.animated-title {
  animation: titleAnimation 1.5s ease-in-out; /* Animación del título */
}

@keyframes titleAnimation {
  0% {
    transform: translateY(-20px); /* Desplazamiento hacia arriba */
    opacity: 0; /* Inicialmente transparente */
  }
  100% {
    transform: translateY(0);
    opacity: 1; /* Totalmente visible */
  }
}

</style>
