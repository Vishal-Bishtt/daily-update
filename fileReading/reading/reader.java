package fileHandling.reading;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class reader {
    public static void main(String[] args) {
        String file = "NewFile.txt";
        try(FileReader reader = new FileReader(file)){
            int read ;
            do{
                read = reader.read();
                System.out.print((char) read);
            }while(read != -1);
        }catch (IOException e){
            System.out.printf("%syou got an error",e.getMessage());
        }

    }
}
