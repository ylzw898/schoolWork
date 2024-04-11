import axiosInstance from './index'

const axios = axiosInstance

export const getBooks = () => { return axios.get(`http://localhost:8000/api/book/`) }

export const postBook = (bookName, bookAuthor) => { return axios.post(`http://localhost:8000/api/book/`, {'comments': bookName, 'author': bookAuthor}) }

export const getRent = () => { return axios.get(`http://localhost:8000/api/rent/`) }

export const getHousePrice = () => { return axios.get(`http://localhost:8000/api/housePrice/`) }

export const postCheck = (id, Region, Garden, Name, Size, Price, Site, Img, Other, Phone) => { return axios.post(`http://localhost:8000/api/check/`, {'id': id, 'region': Region, 'garden': Garden, 'name': Name, 'size': Size, 'price': Price, 'site': Site, 'img': Img, 'other': Other, 'phone': Phone}) }

export const getCheck = () => { return axios.get(`http://localhost:8000/api/check/`) }
