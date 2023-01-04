import java.net.*;
import java.io.*;

class   client
{
    public static void main(String a[])
    {
        System.out.println("Client application is running......");

        Socket s=new Socket("localhost",2100);

        System.out.println("Server is running at port no 2100 and waiting for client request");

        Socket s=ss.accept();
        System.out.println("Request of client accepted ");
        
    }
}