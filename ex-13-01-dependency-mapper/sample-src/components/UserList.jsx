// SAMPLE
import { UserCard } from './UserCard';
import { listUsers } from '../utils/api';

export function UserList() {
  const users = listUsers();
  return users.map(u => UserCard({ id: u.id }));
}
