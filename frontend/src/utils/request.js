import axios from "axios";
import storageService from "@/service/storageService";

const service = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  timeout: 1000 * 5
});

service.interceptors.request.use(
  function(config) {
    Object.assign(config.headers, {
      Authorization: `Bearer ${storageService.get(storageService.USER_TOKEN)}`
    });
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

export default service;
