<template>
    <h2>Search Tool</h2>
    <form class = "search" @submit.prevent = "search">
        <div class="label1">
            <div>
                <label for="department">Department</label>
            <input type="text" id="department" v-model="department">
            </div>
            <div>
                <label for="course_id">Course #</label>
                <input type="text" id="course_id" v-model="course_id">
            </div>
            <label for="course_name">Course Name</label>
            <label for="professor">Professor</label>
        </div>
        <div>
            
            
            <input type="text" id="course_name" v-model="course_name">
            <input type="text" id="professor" v-model="professor">
        </div>

        
        <!-- <input type="text" id="course_id" v-model="course_id"> -->

    </form>
</template>

<script>
    export default {
        data(){
            return {
                department: ''
            };
        },
    methods: {
        search(){

        },
    },
};
</script>

<style scoped>

h2 {
    background-color: aqua;
    font-size: xx-large;
}
.search{
    max-width: 1000px;
    margin: 0 auto;
    background-color: #f5f5f5;
    border: 1px solid #ddd;
}
.label1 {
    display: inline-block;
    font-weight: bold;
}
/* label{
    padding: 10px;
} */

/* input[type="text"]{
    border: 1px solid #ccc;
    border-radius: 3px;
} */

</style>

