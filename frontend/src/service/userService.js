import request from "@/utils/request";

const login = ({ username, password }) => {
  return request.post("token/", { username, password });
};

const user = () => {
  return request.get("user/");
};

export default {
  login,
  user
};
