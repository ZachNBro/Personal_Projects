/**
* File: CrimeData.java
* Author: Zachary N. Brown
* Date: August 10, 2022
* Purpose: This class reads and builds the array of data
* from the Crime.csv file and contains the methods to call
* to calculate the requested data
*/

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class CrimeData {
	
		public ArrayList<USCrimeClass> dataList(){	
			return dataList;
		}
				
		int column = 1; 
				
		// Creates a new array for future data implementation
		ArrayList<USCrimeClass> dataList = new ArrayList<USCrimeClass>();
				
		// Method to create a new constructor for the array and parse the lines of data
		private void buildParseLines(String line) {
				
		USCrimeClass crimeDataForYear = new USCrimeClass(0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
									0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
				
		column = 1;
				
		// Switch method to split and parse data using getter methods in 
		// USCrimeClass and then extract to dataList array
		for (String value : line.split(",")) {
		 	switch (column) {
		 			
				case 1: {
					crimeDataForYear.setYear(Integer.parseInt(value));
					break;
				}
				case 2: {
					crimeDataForYear.setPopulation(Integer.parseInt(value));
					break;
				}
				case 6: {
					crimeDataForYear.setMurderRate(Float.parseFloat(value));
					break;
				}
				case 10: {
					crimeDataForYear.setRobberyRate(Float.parseFloat(value));
					break;
				}
		 		}
		 			
		 		++column;
				}
					
				// Add parsed data from the switch function to the new dataList array
				dataList.add(crimeDataForYear);
				}
				
				// Method to read file
				public void readData(String fileName){
					
				String lineIn = null;  
				BufferedReader fileIn = null;
					
				try {	
						
				fileIn =  new BufferedReader(new FileReader(fileName));
					
				} catch (FileNotFoundException e) {
						e.printStackTrace();
						System.out.println("File Not Found");
				}
							
				// Try block to read each line of the file during buildParseLines method		
				try {    
				    	
					fileIn.readLine();
					lineIn = fileIn.readLine();
				
					while(lineIn != null){ 
							
						buildParseLines(lineIn); 
						lineIn = fileIn.readLine();	
					}
						
				} catch (IOException e) {
				    e.printStackTrace();
					}
				}
		
				// Method to extract year and population data and loop to calculate population growth percentage
				public ArrayList<String> popGrowthRate() {
					
					String tempYears; 
					float tempGrowth; 
					String yearToYearGrowth;
					
					ArrayList<String> growthRateChart = new ArrayList<String>();
				
					growthRateChart.add("****The Year to Year Growth Rates****");
				
					for (int i = 0; i < dataList.size()-1; i++) {
						tempYears = Integer.toString(dataList.get(i).getYear()); 
						tempYears += " - "; 
						tempYears += Integer.toString(dataList.get(i+1).getYear());	
						tempGrowth = (((float)(dataList.get(i+1).getPopulation() -        
								        dataList.get(i).getPopulation()) /
								       (float)(dataList).get(i).getPopulation()))*100; 
							
						yearToYearGrowth = String.format("%s = %.4f%%", tempYears, tempGrowth);
						growthRateChart.add(yearToYearGrowth); 
					}
					
					return growthRateChart;
				}
				
				// Method to extract murder rate data and loop to calculate highest murder rate
				public String murderRateHigh() {
					
					int year = 0;
					float highestRate = 0;
					String murderRateHigh = "\n****The Highest Murder Rate****" + "\n" + "The Year : ";
							
					year = dataList.get(0).getYear();
					highestRate = dataList.get(0).getMurderRate();
					
					for( int i = 1; i < dataList.size(); i++ ){			
						if(highestRate < dataList.get(i).getMurderRate() ){ 
							year = dataList.get(i).getYear();
							highestRate = dataList.get(i).getMurderRate();
						}	
					}
					
					murderRateHigh += Integer.toString(year); 
					murderRateHigh += "\nThe Highest Murder Rate : ";
					murderRateHigh += Float.toString(highestRate);
					
					return murderRateHigh;
				}
				
				// Method to extract murder rate data and loop to calculate lowest murder rate	
				public String murderRateLow() {
					
					int year = 0;
					float highestRate = 0;
					String murderRateLow = "\n****The Lowest Murder Rate****" + "\n" +
									       "The Year : ";
									
					year = dataList.get(0).getYear();
					highestRate = dataList.get(0).getMurderRate();
							
					for( int i = 1; i < dataList.size(); i++ ){	
						if(highestRate > dataList.get(i).getMurderRate() ){ 
							year = dataList.get(i).getYear();
							highestRate = dataList.get(i).getMurderRate();
						}
					}
							
					murderRateLow += Integer.toString(year); 
					murderRateLow += "\nThe Lowest Murder Rate : ";
					murderRateLow += Float.toString(highestRate);
							
							
					return murderRateLow;	
				}
				
				// Method to extract robbery rate data and loop to calculate highest robbery rate
				public String robberyRateHigh() {
					
					int year = 0;
					float highestRate = 0;
					String robberyRateHigh = "****The Highest Robbery Rate****" + "\n" +
				               				 "The Year : ";
					
					year = dataList.get(0).getYear();
					highestRate = dataList.get(0).getRobberyRate();
					
				
					for( int i = 1; i < dataList.size(); i++ ){	
						if(highestRate < dataList.get(i).getRobberyRate() ){ 
							year = dataList.get(i).getYear();
							highestRate = dataList.get(i).getRobberyRate();
						}
					}
					
					robberyRateHigh += Integer.toString(year); 
					robberyRateHigh += "\nThe Highest Robbery Rate : ";
					robberyRateHigh += Float.toString(highestRate);
					
					return robberyRateHigh;
				}
				
				// Method to extract robbery rate data and loop to calculate lowest robbery rate
				public String robberyRateLow() {
						
					int year = 0;
					float highestRate = 0;
					String robberyRateLow = "****The Lowest Robbery Rate****" + "\n" +
											"The Year : ";
					
					year = dataList.get(0).getYear();
					highestRate = dataList.get(0).getRobberyRate();
		
					
					for( int i = 1; i < dataList.size(); i++ ){			
						if(highestRate > dataList.get(i).getRobberyRate() ){
							year = dataList.get(i).getYear();
							highestRate = dataList.get(i).getRobberyRate();
						}
					}
					
					robberyRateLow += Integer.toString(year); 
					robberyRateLow += "\nThe Lowest Robbery Rate : ";
					robberyRateLow += Float.toString(highestRate);
					
					return robberyRateLow;
				}	
}
