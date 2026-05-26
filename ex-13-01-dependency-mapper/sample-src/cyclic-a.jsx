// SAMPLE
import { fromB } from './cyclic-b';

export function fromA() {
  return fromB() + 'A';
}
