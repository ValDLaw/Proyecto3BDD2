<template>
  <div id="app">
    <header>
      <title>Encuentra tu doppelgänger</title>
      <div class="containerA">
        <h1>Encuentra tu doppelgänger</h1>
      </div>
      <nav>
        <ul class="nav-list">
          <li :class="{ active: $route.name === 'SequentialQueueView' }"><router-link :to="{ name: 'SequentialQueueView' }">Sequential Queue</router-link></li>
          <li :class="{ active: $route.name === 'SequentialRangeView' }"><router-link :to="{ name: 'SequentialRangeView' }">Sequential Range</router-link></li>
          <li :class="{ active: $route.name === 'RTreeView' }"><router-link :to="{ name: 'RTreeView' }">R-Tree</router-link></li>
          <li :class="{ active: $route.name === 'HighDView' }"><router-link :to="{ name: 'HighDView' }">High-Dimensional</router-link></li>
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
@import url('https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap');

/* Global styles */
:root {
  --primary-color: #35477d;
  --secondary-color: #9aa5b1;
  --accent-color: #ffcc00;
  --background-color: #f9f9f9;
}

body {
  margin: 0;
  font-family: 'Roboto', sans-serif;
  background-color: var(--background-color);
  color: var(--primary-color);
}

.containerA {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
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
  border: 1px solid var(--primary-color);
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-list li.active a {
  background-color: var(--accent-color);
  /* Estilos adicionales para resaltar el botón activo */
}

.nav-list li a:hover {
  background-color: var(--accent-color);
}

/* Other styles */
h1, h2 {
  color: var(--primary-color);
}

.container {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  margin: 20px;
}

/* Rest of your styles */
/* ... */
</style>
