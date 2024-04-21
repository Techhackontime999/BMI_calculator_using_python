# wap to make a bmi calculator
import os,sys
print(''' Calculate Your Body Mass Index : -> 
*******************************************************
      Body mass index (BMI) is a measure of body fat based on height and weight 
      that applies to adult men and women.
      View the BMI tables or use the tool below to compute yours.\n''')
a=int(input("Enter your age[year] : "))
b=int(input("choose your weight : in kg[enter 1] ,in pound[enter 2] :\n"))

#  BMI Categories:
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater
if b==1:
   w=float(input("Enter your weight here : "))
elif b==2:
      j=float(input("Enter your weight here : "))
      w=j*0.454
else:
      print("invalid input try again . ")       
c=int(input("choose your height : in foot[enter 3] ,in inches[enter 4] ,in m[enter 5] ,in cm[enter 6]:\n"))      
if c==3:
      k=float(input("Enter your height here : "))
      h=(k*12*2.54)/100
elif c==4:
      k=float(input("Enter your height here : "))
      h=(k*2.54)/100
elif c==5:
      h=float(input("Enter your height here : "))
elif c==6:
      h=(float(input("Enter your height here : ")))/100            
else:
      print("invalid input try again . ") 
            
bmi=w/(h**2) 



if bmi<=18.5:
    print("your bmi is :",bmi," , you are in underweight .")
    print('''
*******************************************************          
What Next? Take Action Towards Better Health:

Maintain a Healthy Weight

Maintaining a healthy weight is important for your heart health.
Learn more about underweight
Increase Physical Activity

Moving more can lower your risk factors for heart disease.
Eat a Heart-Healthy Diet

Eating a healthy diet is the key to heart disease prevention.                                                                                                               


Certainly! Here is some information about Body Mass Index (BMI):''')
    

elif 18.5<bmi<=24.9:
        print("your bmi is :",bmi,", you are in normal weight .")
        print('''
*******************************************************
People in this category may be at risk for health issues due to insufficient body weight. Treatment typically involves eating a balanced diet rich in nutrients.
Normal Weight: 18.5 ≤ BMI < 25''')

elif 25<=bmi<=29.9:
      print("your bmi is :",bmi," , you are in overweight .")
      print('''
*******************************************************            
What Next? Take Action Towards Better Health:

Maintain a Healthy Weight

Maintaining a healthy weight is important for your heart health.
Learn more about overweight and obesity
Increase Physical Activity

Moving more can lower your risk factors for heart disease.
Eat a Heart-Healthy Diet

Eating a healthy diet is the key to heart disease prevention.                                                                                                               


Certainly! Here is some information about Body Mass Index (BMI):''') 



else:
      print("your bmi is :",bmi," , you are in obesity[fat state]")
      print('''
*******************************************************            
What Next? Take Action Towards Better Health:

Maintain a Healthy Weight

Maintaining a healthy weight is important for your heart health.
Learn more about overweight and obesity
Increase Physical Activity

Moving more can lower your risk factors for heart disease.
Eat a Heart-Healthy Diet

Eating a healthy diet is the key to heart disease prevention.                                                                                                               


Certainly! Here is some information about Body Mass Index (BMI):
*******************************************************            ''')
      
u=input("type 'yes' for learn more about nutrition + prevention. :\n")
def prevention(bmi):
      if bmi<=18.5:
            print('''
BMI falls into different categories, which are associated with different levels of health risk. Here are the common BMI categories:

Underweight: BMI < 18.5''')
      elif 18.5<bmi<=24.9:
            print('''
People in this category may be at risk for health issues due to insufficient body weight. Treatment typically involves eating a balanced diet rich in nutrients.
Normal Weight: 18.5 ≤ BMI < 25''')
      elif 25<=bmi<=29.9:
            print('''
                  This range is considered healthy for most adults. People in this category are generally at a lower risk of weight-related health issues.
Overweight: 25 ≤ BMI < 30
''')
      else:
            print('''
Individuals in this category have excess weight, which may increase the risk of developing health problems such as heart disease, diabetes, and high blood pressure. Treatment often involves weight loss through diet and exercise.
Obesity: BMI ≥ 30''')
     
def nutrients(bmi):
      if bmi<=18.5:
            print("list of nutrients prefer for you.")
            print('''
For Underweight (BMI < 18.5):
*******************************************************                  
Nutrients to Focus on:

1.Calories: Increase overall calorie intake to support weight gain.
2.Protein: Essential for muscle repair and growth.
3.Healthy Fats: Provide concentrated calories for weight gain and support overall health.
4.Carbohydrates: Choose complex carbohydrates for sustained energy.
Prevention Tips:

1.Healthy Fats: Include sources such as nuts, seeds, avocados, and olive oil.
2.Protein-Rich Foods: Lean meats, fish, poultry, legumes, and dairy products.
3.Nutrient-Dense Foods: Focus on whole grains, fruits, vegetables, and dairy or non-dairy alternatives.
4.Regular Meals and Snacks: Aim for balanced meals and snacks throughout the day.
5.Avoid Empty Calories: Minimize sugary drinks and snacks.''')

      elif 18.5<bmi<=24.9:
            print("list of nutrients prefer for you.")
            print('''
For Normal Weight (BMI 18.5 - 24.9):
*******************************************************                  
Nutrients to Focus on:

1.Balanced Diet: Aim for a mix of all essential nutrients.
2.Fiber: Important for digestive health and feeling full.
3.Antioxidants: Found in fruits and vegetables, help protect cells from damage.
4.Omega-3 Fatty Acids: Support heart and brain health.
Prevention Tips:

1.Variety in Diet: Include a wide range of fruits, vegetables, whole grains, lean proteins, and healthy fats.
2.Portion Control: Be mindful of portion sizes to maintain a healthy weight.
3.Physical Activity: Regular exercise is key to overall health and weight maintenance.
4.Hydration: Drink plenty of water throughout the day.
5.Limit Processed Foods: Opt for whole, unprocessed foods whenever possible.
''')
      elif 25<=bmi<=29.9:
            print("list of nutrients prefer for you.")
            print('''
For Overweight (BMI 25 - 29.9):
*******************************************************                  
Nutrients to Focus on:

1.Fiber: Helps with satiety and digestive health.
2.Lean Proteins: Supports muscle mass while reducing excess calories.
3.Complex Carbohydrates: Provides sustained energy without spiking blood sugar.
4.Calcium and Vitamin D: Important for bone health.
Prevention Tips:

1.Calorie Awareness: Be mindful of portion sizes and overall calorie intake.
2.Physical Activity: Aim for regular exercise, including both cardio and strength training.
3.Healthy Snacking: Opt for fruits, vegetables, nuts, or yogurt instead of processed snacks.
4.Meal Planning: Prepare meals at home to control ingredients and portions.
5.Mindful Eating: Pay attention to hunger and fullness cues to avoid overeating.
''')
      else:
            print("list of nutrients prefer for you.")
            print('''
For Obesity (BMI 30+):
*******************************************************                  
Nutrients to Focus on:

1.High-Quality Protein: Supports muscle mass during weight loss.
2.Fiber: Aids in digestion and helps with feelings of fullness.
3.Healthy Fats: Supports heart health and provides satiety.
4.Whole Grains: Provides sustained energy without rapid blood sugar spikes.
Prevention Tips:

1.Medical Guidance: Consider working with a healthcare provider or dietitian for a personalized plan.
2.Behavioral Changes: Focus on lifestyle changes for long-term success.
3.Regular Exercise: Incorporate both aerobic and strength-training exercises.
4.Balanced Meals: Opt for meals that include a variety of nutrients to support overall health.
5.Mindful Eating: Practice eating slowly, savoring each bite, and paying attention to hunger and fullness cues.
Remember, these are general guidelines. Individual nutritional needs may vary, and it's always best to consult with a healthcare professional before making significant changes to your diet or lifestyle.
''')
if u=="yes":
      nutrients(bmi)

s=input("tap yes to know more info....... . :\n")                          
if s=="yes":
      prevention(bmi)

print("************************************************************************************************************************************************************************")





      









    