import { api } from "../APIConfig";

export const calculate = async (requestBody) => {
  try {
    const res = await api.post("/calculate", requestBody);
    return res.data;
  } catch (err) {
    return err.response.data;
  }
};

export const getHistory = async (requestBody) => {
  try {
    const res = await api.post("/history", requestBody);
    return res.data;
  } catch (err) {
    return err.response.data;
  }
};
