<template>
    <div id="app">
        <textarea rows="10" v-model="text"></textarea>
        <br>
        <FileReader @load="text = $event"></FileReader>
    </div>
</template>

<script>
    import FileReader from "./components/FileReader";

    export default {
        name: 'App',
        data: () => ({text: ""}),
        components: {
            FileReader
        }
    }
</script>

<style>

</style>
