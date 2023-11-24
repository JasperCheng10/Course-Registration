import "./assets/main.css";

//Added for Auth) login
// import { createAuth0 } from '@auth0/auth0-vue'

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

//Original app.use()
app.use(router);

//Auth0 app.use()
// app.use(
//     createAuth0({
//         domain:"dev-gi0zusfv0z1zvt1x.us.auth0.com",
//         clientId: "clCyl1SjISWMmL2iMStXnQzHTBy44wwq",
//         authorizationParams: {
//             redirect_uri: window.location.origin
//         }
//     })
// );


app.mount("#app");
