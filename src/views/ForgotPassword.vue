<template>
    <h1>Reset Password</h1>
    <p>Enter email associated with your account to reset your password.</p>
    <div class = "forgotpassword">
        <form @submit.prevent="forgotpassword">
            <div class="form-group">
                <label for = "email">Email:</label>
                <input type="email" id="email" v-model="email" required>
            <div>
                <button type="sumbit">
                    Submit
                </button>   
            </div>
            </div>
        </form>

    </div>
</template>

<script>
export default{
    name: "Forgot Password",
    data(){
        return {
            email: ""
        };
    },
    methods: {
        forgotpassword(){
            //IDK
        },
    },
};
</script>

<style scoped>

h1 {
    font-size: x-large;
    background-color: #007BFF;
    color:#fff;
    padding: 20px;
    margin-bottom: 75px;
    border-color: black;
    border-width: 2px;
}

p {
    text-align: center;
}
.forgotpassword {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.form-group{
    margin-bottom: 20px;
}

label {
    display: block;
    font-weight: bold;
}
                                                                                                                                               
input[type="text"],
input[type="email"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
}

button{
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer     ;
}

</style>