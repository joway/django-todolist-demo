import axios from 'axios'

let baseAPI = 'http://127.0.0.1:8000/api'
if (process.env.NODE_ENV === 'production') {
  baseAPI = 'http://todo.sh.mk/api'
}

const opts = {
  withCredentials: true,
  timeout: 1000,
}

const APIService = {
  getTodoLists: () => {
    const path = '/list'
    return axios.get(`${baseAPI}${path}`, {}, opts)
  },
  getTodoList: (name) => {
    const path = `/list/${name}`
    return axios.get(`${baseAPI}${path}`, {}, opts)
  },
  createTodoList: (name) => {
    const path = '/list'
    return axios.post(`${baseAPI}${path}`, {
      name,
    }, opts)
  },
  updateItem: (id, content, done) => {
    const path = `/item/${id}`
    return axios.put(`${baseAPI}${path}`, {
      content, done,
    }, opts)
  },
  crateItem: (content, done) => {
    const path = '/item'
    return axios.post(`${baseAPI}${path}`, {
      content, done,
    }, opts)
  },
  updateList: (name, items) => {
    const path = `/list/${name}`
    return axios.put(`${baseAPI}${path}`, {
      items,
    }, opts)
  },
}

export default APIService
