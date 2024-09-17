"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number of words per line in the text file in the following
format:

"Average words per line: [average]"
"""
import argparse
import text_utils
def averagewords_perline(filename):
  """
  Reference the "Reading Files in Python" lesson to open the `file.txt` file, count the number of words in the file, and return the count:
  """
  #open the file 
  file = open(filename, 'r')
  #read all lines into a list
  lines = file.readlines()
  x=0 
  water=0
  #itterate over each line 
  for line in lines:
    x=x+1 
    water = water+text_utils.count_words(line)
  
  #close the file
  file.close()
  return water // x

def main():
  parser = argparse.ArgumentParser(description='count lines in file.')
  parser.add_argument('filename', help='The file to count lines from')
  args = parser.parse_args()


  count = averagewords_perline(args.filename)
  print(f"Average words per line: {count}")
 

if __name__ =='__main__':
  main()

