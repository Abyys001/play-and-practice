import java.util.*;

public class Main {

    public static void main(String[] args) {
        Stack<Character> stack = new Stack<Character>();
        Scanner input = new Scanner(System.in);
        boolean flag = true;
         while (flag) { // 0 input for exit
            System.out.println("enter '(' or ')'  or 0 for exit");
            String txt = input.nextLine();

            if (txt == "0"){
                break;
            }

            char chr = txt.charAt(0); // convert input form String to char

            if (chr == '('){
                stack.push(chr);
            }
            else if(chr == ')' && stack.isEmpty() == false){
                stack.pop();
            }
            else{ // if user enters non-valid value, the programm will stop
                break;
            }
            
        }
        if (stack.isEmpty()){
            System.out.println("Balanced");
        }
        else{
            System.out.println("Unbalanced");
        }

        input.close();
    }
}
