/**
* File: StateChangeable.java
* Author: Zachary N. Brown
* Date: October 13, 2022
* Purpose: This interface that specifies the bounded
* generic type parameter <T> as an enumerated type and
* the abstract method to change the state of the property
*/

public interface StateChangeable<T> {

	public static <T extends Enum<T>> T valueOf(Class <T> enumType, String name) {	
		T value = Enum.valueOf(enumType, name);
		return value;
	}
	
	abstract void changeState(T status);		
}

