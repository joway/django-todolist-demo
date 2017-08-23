<template>
  <el-row style="margin: 32px;">
    <h1>{{ name }}</h1>
    <el-row v-for="(item, index) in items" :key="index" style="margin-bottom: 12px;">
      <el-col :span="12" :offset="6">
        <el-input v-model="item.content" :disabled="item.done" @change="updateItemContent(item.id, item.content, item.done)"></el-input>
      </el-col>
      <el-col :span="1">
        <el-button type="success" :icon="item.done ? 'close' : 'check'" @click="updateItem(item.id, item.content, !item.done)" v-if="item.id"></el-button>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="1" :offset="18">
        <el-button type="primary" icon="plus" @click="addItem"></el-button>
      </el-col>
    </el-row>

    <el-row style="margin-top: 32px;">
      <el-col :span="1" :offset="18">
        <el-button type="warning" icon="document" @click="saveTodoList">保存</el-button>
      </el-col>
    </el-row>
  </el-row>
</template>

<script>
import APIService from '../api'

export default {
  name: 'detail',
  data() {
    return {
      name: '',
      items: [],
    }
  },
  async created() {
    await this.reloadData()
  },
  methods: {
    async reloadData() {
      const name = this.$route.params.name
      try {
        this.items = (await APIService.getTodoList(name)).data.items
        this.name = name
      } catch (e) {
        await APIService.createTodoList(name)
        this.reloadData()
      }
    },
    redirectTo(path) {
      if (this.inputName.length <= 0) {
        this.$message.error('请输入 Name')
      } else {
        this.$router.push(path)
      }
    },
    async addItem() {
      const item = (await APIService.crateItem('', false)).data
      this.items.push(item)
    },
    async updateItem(id, content, done) {
      try {
        await APIService.updateItem(id, content, done)
        await this.reloadData()
        this.$message.success({
          message: '更新成功',
          duration: 1000,
        })
      } catch (e) {
        this.$message.success('更新失败')
      }
    },
    async updateItemContent(id, content, done) {
      try {
        await APIService.updateItem(id, content, done)
      } catch (e) {
        this.$message.success('更新失败')
      }
    },
    async saveTodoList() {
      const itemsIds = []
      this.items.forEach(item => (itemsIds.push(item.id)))
      try {
        await APIService.updateList(this.name, itemsIds)
        await this.reloadData()
        this.$message.success({
          message: '更新成功',
          duration: 1000,
        })
      } catch (e) {
        this.$message.success('更新失败')
      }
    },
  },
}
</script>

<style scoped>
.todo-list {
  text-decoration: none;
  border-bottom: 3px solid gray;
}

.todo-list:hover {
  color: hotpink;
}
</style>
