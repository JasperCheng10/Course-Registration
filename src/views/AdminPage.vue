<template>
    <div class="navigation_bar">
        <a class="link" href="">Search</a>
        <a class="link" href="/admin/createcourse">Create Course</a>
    </div>

    <div class="search">
        <form @search.prevent="search">
            <div class="form-group">
                <label for="department">Department</label>
                <input type="text" id="department" v-model="department" required>
                <label for="course_id">Course #</label>
                <input type="text" id="course_id" v-model="course_id">
                <label for="course_name">Course Name</label>
                <input type="text" id="course_name" v-model="course_name">
                <label for="professor">Professor</label>
                <input type="text" id="professor" v-model="professor">
            </div>

        </form>
    </div>


    <h1>Hello World</h1>
</template>


<script>
export default{
    data(){
        return{
            department: "",
            course_id: "",
            course_name: "",
            professor: "",
            start_time: "",
            end_time: "",
            days: "",
            location: "",
            credits: "",
            course_type: "",
            prerequisite: ""
        };
    },
    methods: {
        search(){
            //Back-End search
        },
    },
};
</script>   

<style scoped>

.navigation_bar{
    background-color: f5f5f5;
}

.link{
    font-family: 'Bebas Neue', sans-serif;
    color: black;
    font-size: large;
    font-weight: bold;
    text-decoration: none;
    padding: 10px;
    
}

.link:hover{
    color: #1e9fe1;
}

.search{
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f5f5f5;
}


.form-group {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 20px;
}

.form-group input {
    flex: 1;
}

label {
    display: block;
    font-weight: bold;
}

input[type="text"] {
    width: 100px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
}

</style>