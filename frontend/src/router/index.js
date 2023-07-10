import { createRouter, createWebHistory } from 'vue-router';
import MenuView from '@/views/MenuView.vue';
import SequentialQueueView from '@/views/ApiView'
import SequentialRangeView from '@/views/ApiView'
import RTreeView from '@/views/ApiView'
import HighDView from '@/views/ApiView'

const routes = [
    {
        path: '/',
        name: 'MenuView',
        component: MenuView
    },
    {
      path: '/sequential_queue',
      name: 'SequentialQueueView',
      component: SequentialQueueView
    },
    {
      path: '/sequential_range',
      name: 'SequentialRangeView',
      component: SequentialRangeView
    },
    {
      path: '/rtree',
      name: 'RTreeView',
      component: RTreeView
    },
    {
      path: '/highd',
      name: 'HighDView',
      component: HighDView
    }
  ];
  
  const router = createRouter({
    history: createWebHistory(),
    routes
  });
  
  export default router;