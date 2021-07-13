public class Hello {
    public static void main(String[] args){
        // public is an access modifier defining the class
        // we need to have static for java to find our method to run the code.
        // void means function will not return any value.
        System.out.println("Hello World");
        int minvalue = Integer.MIN_VALUE;
        int maxvalue = Integer.MAX_VALUE;

        System.out.println("The Max Integer Value is:-  " + maxvalue);
        System.out.println("The Min Integer Value is:- " + minvalue);

        // taking more than maxvalue will result in overflow error.
        // taking less then minvalue will result in underflow error.

        byte min_byte_value = Byte.MIN_VALUE;
        byte max_byte_value = Byte.MAX_VALUE;

        System.out.println("The Max Byte Value is:-  " + max_byte_value);
        System.out.println("The Min Byte Value is:-  " + min_byte_value);

        short min_short_value = Short.MIN_VALUE;
        short max_short_value = Short.MAX_VALUE;

        System.out.println("The Max Short Value is:-  " + max_short_value);
        System.out.println("The Min Short Value is:-  " + min_short_value);

        long max_long_value = Long.MAX_VALUE;
        long min_long_value = Long.MIN_VALUE;

        System.out.println("The Max Long Value is:-  " + max_long_value);
        System.out.println("THe Min Long Value is:-  " + min_long_value);

        // type casting and explicit conversion.

        int total = (int)(max_short_value);

        byte byte_total = (byte)(maxvalue/2);

        System.out.println(total);
        System.out.println(byte_total);

        double max_double_value = Double.MAX_VALUE;
        double min_double_value = Double.MIN_VALUE;

        System.out.println("The Max Double Value:-  " + max_double_value);
        System.out.println("The Min Double Value:-  " + min_double_value);

    }
}
