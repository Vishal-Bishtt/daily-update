package fileHandling.writing;

import java.io.FileWriter;
import java.io.IOException;

public class writing {
    public static void main(String[] args) {
        String name = "NewFile.txt";
        try{
            FileWriter writer = new FileWriter(name);
            writer.write("This is my first file in java.");
            writer.flush();
            System.out.println("The file has been flushed");
        }catch(IOException e){
            System.out.printf("%sAn error has occured!!",e.getMessage());
        }

    }
}
