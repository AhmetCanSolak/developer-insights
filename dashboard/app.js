const baseURL = "https://api.github.com/repos/atom/atom";

const Responses = {

        template: '#responses-template',

        data: () => ({

        }),

        mounted() {

        },

        methods: {

        }
};

Vue.component('responses', Responses);

const NotFound = { template: '<p>Page not found</p>' }
const Home = { template: '<p>home page</p>' }
const About = { template: '<p>about page</p>' }

const routes = {
  '/'      : Responses,
  '/first' : Responses,
  '/dashboard/' : Responses,
  '/second': Responses,
  '/third' : Responses,
  '/about' : About
}

new Vue({
  el: '#app',
  data: {
      currentRoute: window.location.pathname
  },
  computed: {
      ViewComponent () {
        console.log(this.currentRoute);
        return routes[this.currentRoute] || NotFound
      }
  },
  render (h) { return h(this.ViewComponent) }
});
