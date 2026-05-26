// SAMPLE
import { fromA } from './cyclic-a';

export function fromB() {
  return fromA() + 'B';
}
