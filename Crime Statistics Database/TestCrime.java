/**
* File: TestCrime.java
* Author: Zachary N. Brown
* Date: August 10, 2022
* Purpose: To create new objects to store data from
* the CrimeData class, initiate the Menu from the
* Menu class and keep track of time while using the
* program
*/

public class TestCrime {
		
		// Private variables for timer
		private static double startTime = 0.0;
		private static double endTime = 0.0;
			
		public static void main(String[] args) {
				
		setStartTime();
			
		// Create new CrimeData object to store data and command-line argument to send in file
		CrimeData initiateData = new CrimeData();
		initiateData.readData(args[0]);
			
		// Create new Menu object to initiate user menu for data selection
		Menu userMenu = new Menu(initiateData);
		userMenu.menu();
		setEndTime();
		System.out.println(elapsedTime());
		}
	
		// Timer methods
		public static void setStartTime() {
			startTime = System.nanoTime();
		}
		public static double getStartTime() { 
			return startTime;
		}
			
		public static void setEndTime() {
			endTime = System.nanoTime();
		}
		public static double getEndTime() { 
			return endTime;
		} 
			
		// String method to display elapsed time to user upon completion
		public static String elapsedTime(){
	    	double time = (getEndTime() - getStartTime())/1000000000.0; 
	    	String elapsedTime = ("\n***Elapsed Time: " + Math.round(time) + " seconds***\n");
	    	elapsedTime += "***Thank you for using the US Crime Statistics Program***\n\n";
	    		
	    	return elapsedTime;		
		}		
}

