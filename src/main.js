import "./assets/main.css";

//Added for Auth) login
import { createAuth0 } from '@auth0/auth0-vue'

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

//From Lab
app
    .use(router)
    .use(
        createAuth0({
            domain: import.meta.env.VITE_AUTH0_DOMAIN,
            clientId: import.meta.env.VITE_AUTH0_CLIENT_ID,
            authorizationParams: {
                audience: import.meta.env.VITE_AUTH0_AUDIENCE,
                redirect_uri: import.meta.env.VITE_AUTH0_CALLBACK_URL,
            },
        })
    )

app.mount("#app");
