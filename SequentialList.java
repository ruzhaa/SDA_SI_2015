package sda_1;

public class SequentialList implements ListInterface {
	private int size;
	private int capacity = 10;
	private int[] array;

	public SequentialList() {
		size = 0;
		array = new int[capacity];
	}

	private void tryGrow() {
		if (size == capacity) {
			int[] newArray = new int[(capacity * 2)];
			for (int i = 0; i < size; i++) {
				newArray[i] = array[i];
			}
			array = newArray;
		}
	}

	public void add(int newElement) {
		tryGrow();
		array[size] = newElement;
		size++;
	}

	public int get(int index) {
		return array[index];
	}

	public void insert(int newElement, int index) {
		if (index <= size) {
			int[] temp = new int[size + 1];
			for (int i = 0; i < index; i++) {
				temp[i] = array[i];
			}
			temp[index] = newElement;
			for (int i = index; i < size; i++) {
				temp[i + 1] = array[i];
			}
			array = temp;
			size++;
		} else {
			add(newElement);
		}

		// System.out.println(size);
	}

	public int indexOf(int element) {
		for (int i = 0; i < size; i++) {
			if (array[i] == element) {
				return i;
			}
		}
		return -1;

	}

	public SequentialList copy() {
		SequentialList newList = new SequentialList();
		for (int i = 0; i < size; i++) {
			newList.add(array[i]);
		}
		return newList;
	}

	public void print() {
		for (int i = 0; i < size - 1; i++) {
			System.out.print(array[i] + ", ");
		}
		System.out.println(array[size - 1]);
	}

	public void deleteAt(int index) {
		int[] temp = new int[size - 1];
		for (int i = 0; i < index; i++) {
			temp[i] = array[i];
		}
		for (int i = index + 1; i < size; i++) {
			temp[i - 1] = array[i];
		}
		array = temp;
		size--;
	}

	public boolean removeElement(int element) {
		for (int i = 0; i < size; i++) {
			if (array[i] == element) {
				deleteAt(i);
				return true;
			}
		}
		return false;
	}

	public SequentialList reverse() {
		SequentialList newList = new SequentialList();
		for (int i = 0; i < size / 2; i++) {
			int temp = array[i];
			array[i] = array[size - i - 1];
			array[size - i - 1] = temp;
			newList.add(temp);
		}
		return newList;
	}

	public boolean equals(SequentialList otherList) {
		for (int i = 0; i < size; i++) {
			if (array[i] == otherList.get(i)) {
				return true;
			}
		}
		return false;
	}

	public SequentialList removeDuplicates() {
		return null;
	}

	public void splice(SequentialList otherList, int start, int end) {
		for (int i = start; i < end; i++) {
			int element = otherList.get(i);
			add(element);
		}
	}

	public SequentialList splitAt(int index) {
		return null;
	}
}
