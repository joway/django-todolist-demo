<template>
  <el-row style="margin: 32px;">
    <h1>TodoList</h1>
    <el-row>
      <el-col :span="4" :offset="10">
        <el-input v-model="inputName" placeholder="请输入名称"></el-input>
      </el-col>
      <el-col :span="2">
        <el-button type="primary" @click="redirectTo(`${inputName}`)">创建</el-button>
      </el-col>
    </el-row>

    <el-row v-for="list in todoLists" :key="list.name">
      <h2>
        <router-link :to="list.name" class="todo-list">{{ list.name }}</router-link>
      </h2>
    </el-row>
  </el-row>
</template>

<script>
import APIService from '../api'

export default {
  name: 'home',
  data() {
    return {
      inputName: '',
      todoLists: [],
    }
  },
  async created() {
    this.todoLists = (await APIService.getTodoLists()).data
  },
  methods: {
    redirectTo(path) {
      if (this.inputName.length <= 0) {
        this.$message.error('请输入 Name')
      } else {
        this.$router.push(path)
      }
    },
  },
}
</script>

<style scoped>
.todo-list{
  text-decoration: none;
  border-bottom: 3px solid gray;
}
.todo-list:hover {
    color: hotpink;
}
</style>
