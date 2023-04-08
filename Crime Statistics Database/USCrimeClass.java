/**
* File: TestCrime.java
* Author: Zachary N. Brown
* Date: August 10, 2022
* Purpose: Provides the private fields, constructor,
* and methods to call for the necessary data used in 
*/

public class USCrimeClass {

			// Private fields
			private int year;
			private int population;
			private int violentCrime;
			private float violentCrimeRate;
			private int murder;
			private float murderRate;
			private int rape;
			private float rapeRate;
			private int robbery;
			private float robberyRate;
			private int aggravatedAssualt;
			private float aggravatedAssualtRate;
			private int propertyCrime;
			private float propertyCrimeRate;
			private int burglary;
			private float burglaryRate;
			private int larcenyTheft;
			private float larcenyTheftRate;
			private int motorVehicleTheft;
			private float motorVehicleTheftRate;
			  
			// Constructor
			public USCrimeClass (int year, int population, int violentCrime, float violentCrimeRate, 
					int murder, float murderRate, int rape, float rapeRate, int robbery, float robberyRate, int aggravatedAssault,
					float aggravatedAssaultRate, int propertyCrime, float propertyCrimeRate, int burglary, float burglaryRate,
					int larcenyTheft, float larcenyTheftRate, int motorVehicleTheft, float motorVehicleTheftRate) {
		
			this.year = year;
			this.population = population;
			this.violentCrime = violentCrime;
			this.violentCrimeRate = violentCrimeRate;
			this.murder = murder;
			this.murderRate = murderRate;
			this.rape = rape;
			this.rapeRate = rapeRate;
			this.robbery = robbery;
			this.robberyRate = robberyRate;
			this.aggravatedAssualt = aggravatedAssault;
			this.aggravatedAssualtRate = aggravatedAssaultRate;
			this.propertyCrime = propertyCrime;
			this.propertyCrimeRate = propertyCrimeRate;
			this.burglary = burglary;
			this.burglaryRate = burglaryRate;
			this.larcenyTheft = larcenyTheft;
			this.larcenyTheftRate = larcenyTheftRate;
			this.motorVehicleTheft = motorVehicleTheft;
			this.motorVehicleTheftRate = motorVehicleTheftRate;		
			}
		
			// Getter methods
			public int getYear() {
			return year;
			}
		
			public long getPopulation() {
			return population;
			}
			
		    public int getViolentCrime() {
		        return violentCrime;
		    }

		    public float getViolentCrimeRate() {
		        return violentCrimeRate;
		    }

		    public int getMurder() {
		        return murder;
		    }
		    
		    public float getMurderRate() {
				return murderRate;
			}

		    public int getRape() {
		        return rape;
		    }

		    public float getRapeRate() {
		        return rapeRate;
		    }

		    public int getRobbery() {
		        return robbery;
		    }
		    
		    public float getRobberyRate() {
				return robberyRate;
			}

		    public int getAggravatedAssualt() {
		        return aggravatedAssualt;
		    }

		    public float getAggravatedAssualtRate() {
		        return aggravatedAssualtRate;
		    }

		    public int getPropertyCrime() { 
				return propertyCrime;
		    }

		    public float getPropertyCrimeRate() {
				return propertyCrimeRate;
		    }

		    public int getBurglary() {    
				return burglary;
		    }

		    public float getBurglaryRate() {  
				return burglaryRate;
		    }

		    public int getLarcenyTheft() {
				return larcenyTheft;
		    }

		    public float getLarcenyTheftRate() {
		       	return larcenyTheftRate;
		    }

		    public int getMotorVehicleTheft() {
				return motorVehicleTheft;
		    }

		    public float getMotorVehicleTheftRate() {  
				return motorVehicleTheftRate;
		    }
		    
			    // Setter methods
				public void setYear(int year) {
					this.year = year;
				}
				
				public void setPopulation(int population) {
					this.population = population;
				}
				
				public void setViolentCrime(int violentCrime) {
					this.violentCrime = violentCrime;
				}
				
				public void setViolentCrimeRate(float violentCrimeRate) {
					this.violentCrimeRate = violentCrimeRate;
				}
				
				public void setMurder(int murder) {
					this.murder = murder;
				}
				
				public void setMurderRate(float murderRate) {
					this.murderRate = murderRate;
				}
				
				public void setRobbery(int robbery) {
					this.robbery = robbery;
				}
				
				public void setRobberyRate(float robberyRate) {
					this.robberyRate = robberyRate;
				}	
				
				public void setAggravatedAssault(int aggravatedAssault) {
					this.aggravatedAssualt = aggravatedAssault;
				}	
				
				public void setAggravatedAssaultRate(float aggravatedAssaultRate) {
					this.aggravatedAssualtRate = aggravatedAssaultRate;
				}	
			
				public void setPropertyCrime(int propertyCrime) {
					this.propertyCrime = propertyCrime;
				}
				
				public void setPropertyCrimeRate(float propertyCrimeRate) {
					this.propertyCrimeRate = propertyCrimeRate;
				}
				
				public void setBurglary(int burglary) {
					this.burglary = burglary;
				}
				
				public void setBurglaryRate(float burglaryRate) {
					this.burglaryRate = burglaryRate;
				}
				
				public void setlarcenyTheft(int larcenyTheft) {
					this.larcenyTheft = larcenyTheft;
				}
				
				public void setlarcenyTheftRate(float larcenyTheftRate) {
					this.larcenyTheftRate = larcenyTheftRate;
				}
				
				public void setMotorVehicleTheft(int motorVehicleTheft) {
					this.motorVehicleTheft = motorVehicleTheft;
				}
				
				public void setMotorVehicleTheftRate(float motorVehicleTheftRate) {
					this.motorVehicleTheftRate = motorVehicleTheftRate;
				}
}
