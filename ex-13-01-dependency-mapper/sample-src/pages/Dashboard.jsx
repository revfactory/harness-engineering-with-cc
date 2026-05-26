// SAMPLE
import { UserList } from '../components/UserList';
import { Header } from '../components/Header';

export function Dashboard() {
  return Header() + UserList();
}
