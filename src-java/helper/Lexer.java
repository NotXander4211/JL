package helper;
import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class Lexer{
    public static File mainfile = new File("./test.jail");
    public static ArrayList<String> program = new ArrayList<>();
    public static int lc = -1;
    public static HashMap<String, String> labelCounter = new HashMap<>();
    public static String[] curLine;
    public static String opcode = "";

    public Lexer(String fn){
        mainfile = new File(fn);
    }

    public static void readFile(){
        try {
            Scanner fileReader = new Scanner(mainfile);
            while(fileReader.hasNextLine()){
                lc++;
                curLine = fileReader.nextLine().split(" ");
                opcode = curLine[0].toLowerCase();
                if (opcode.endsWith(":")){
                    labelCounter.put(opcode.split(":")[0], Integer.toString(lc));
                    continue;
                } else if (opcode == ""){
                    continue;
                }
                program.add(opcode);
                //System.out.println(opcode + ":");
                if (opcode.equals("push")){
                    // expect int next
                    //System.out.println(opcode + ">>>>>");
                    String num = curLine[1];
                    program.add(num);
                    lc++;
                    continue;
                } else if (opcode.equals("print")){
                    // expect string next
                    //System.out.println(opcode + ">>>>>");
                    String strL = String.join(" ", Arrays.copyOfRange(curLine, 1, curLine.length));
                    program.add(strL);
                    lc++;
                    continue;
                } else if (opcode.equals("jump.eq.0")){
                    // expect string next
                    //System.out.println(opcode + ">>>>>");
                    String label = curLine[1].toLowerCase();
                    program.add(label);
                    lc++;
                    continue;
                }
            }
            fileReader.close();
        } catch (Exception e){
            System.out.println(e.toString());
        }
    }

    public ArrayList<String> getProgram(){
        readFile();
        return program;
    }
    public HashMap<String, String> getLabelCounter(){
        return labelCounter;
    }

    // public static void main(String[] args){
    //     readFile();
    //     String listString = String.join(", ", program);
    //     System.out.println(listString);
    // }
}