<template>
    <h2 id="search_header">Search</h2>
    <form class = "search" @submit.prevent = "search">
        <!-- Course ID
        Course Name
        Professor
        Course Type
        Content Area
        Credits -->
            <table>
            <tr>
                <th>
                    <label for="course_id">Course_Id</label>
                    <input type="text" id="course_id" v-model="course_id">
                </th>
                <th>
                    <label for="course_name">Course Name</label>
                    <input type="text" id="course_name" v-model="course_name">
                </th>
                <th>
                    <label for="course_type">Course Type</label>
                    <input type="text" id="course_type" v-model="course_type">
                </th>
            </tr>
            <tr>
                <th>
                    <label for="credit">Credits</label>
                    <input type="text" id="credits" v-model="credits">
                </th>
                <th>
                    <label for="content_area">Content Area</label>
                    <input type="text" id="content_area" v-model="content_area">
                </th>
                <th>
                    <label for="professor">Professor</label>
                <input type="text" id="professor" v-model="professor">
                </th>
            </tr>
        </table>
        <div id="button_container">
            <button type="submit" id="search_tool">Search</button>
        </div>
    </form>
    <div>
        <h2 id="search_result_header">Search Results</h2>
        
    </div>




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
    font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: xx-large;
    font-weight: bold;
    margin-left: 391px;
}
.search{
    max-width: 700px;
    margin: 0 auto;
    background-color: #f5f5f5;
    border: 1px solid #ddd;

}

table {
    display: block;
    justify-content: center;
    margin-bottom: 20px;
    border: #ccc;
}

td{
    width: 100%;
}

label{
    display: block;
    font-weight: bold;
    padding: 10px;
    text-align: left;
}

input[type="text"]{
    border: 1px solid #ccc;
    border-radius: 3px;
    margin-left: 10px;
    margin-right: 10px;
}

#button_container{
    display: flex;
    justify-content: flex-end;
    margin-right: 15px;
    margin-bottom: 10px;  
}

button {
    color: #fff;
    background-color: #007BFF;
    padding: 10px 20px;
    border-color: black;
    border-width: 1px;
    border-radius: 10px;
    
}

</style>

