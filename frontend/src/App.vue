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
.containerA {
  display: flex;
  justify-content: center;
  align-items: center;
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
  color: #333;
  padding: 5px 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.nav-list li.active a {
  background-color: #f0f0f0;
  /* Estilos adicionales para resaltar el botón activo */
}

.nav-list li a:hover {
  background-color: #f0f0f0;
}
</style>
