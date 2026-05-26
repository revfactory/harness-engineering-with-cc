// SAMPLE
import { request } from './http';

export function getUser(id) {
  return request(`/users/${id}`);
}

export function listUsers() {
  return request('/users');
}
