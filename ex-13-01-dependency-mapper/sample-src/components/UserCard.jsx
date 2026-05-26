// SAMPLE
import { useAuth } from '../hooks/useAuth';
import { formatDate } from '../utils/format';

export function UserCard({ id }) {
  const user = useAuth(id);
  return user ? user.name + ' ' + formatDate(new Date()) : null;
}
