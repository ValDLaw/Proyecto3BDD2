import { createRouter, createWebHistory } from 'vue-router';
import MenuView from '@/views/MenuView.vue';
import FaissView from '@/views/FaissView'
import SequentialView from '@/views/SequentialView'
import RTreeView from '@/views/RTreeView'
import KDTreeView from '@/views/KDTreeView'

const routes = [
    {
        path: '/',
        name: 'MenuView',
        component: MenuView
    },
    {
      path: '/sequential',
      name: 'SequentialView',
      component: SequentialView
    },
    {
      path: '/faiss',
      name: 'FaissView',
      component: FaissView
    },
    {
      path: '/rtree',
      name: 'RTreeView',
      component: RTreeView
    },
    {
      path: '/kdtree',
      name: 'KDTreeView',
      component: KDTreeView
    }
  ];
  
  const router = createRouter({
    history: createWebHistory(),
    routes
  });
  
  export default router;