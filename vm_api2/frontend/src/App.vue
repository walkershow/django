<template>
  <div class="continer-fluid">
    <div class="row text-center h1">
      VM STAT2
    </div>
    <hr />
    <div class="row">
      <div class="col-md-3">
        <codelist> </codelist>
      </div>
    </div>
  </div>
</template>
<script>
import codelist from "./components/list.vue";
export default {
  name: "app",
  components: {
    codelist
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  webkit-font-smoothing: antialiased;
  moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
