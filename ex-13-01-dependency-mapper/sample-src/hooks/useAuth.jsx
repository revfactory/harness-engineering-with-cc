// SAMPLE
import { getUser } from '../utils/api';

export function useAuth(id) {
  return getUser(id);
}
