const PREFIX = "";

const USER_PREFIX = `${PREFIX}user_`;

const USER_TOKEN = `${USER_PREFIX}token`;
const USER_NAME = `${USER_PREFIX}name`;

const set = (key, data) => {
  localStorage.setItem(key, data);
};

const get = key => localStorage.getItem(key);

export default {
  set,
  get,
  USER_TOKEN,
  USER_NAME
};
