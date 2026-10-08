public class Test {
    public static void main(String[] args) {
        byte[] b = java.util.Base64.getDecoder().decode("AQID");
        java.io.InputStream is = new java.io.ByteArrayInputStream(b);
        System.out.println("Java Base64 works! bytes=" + b.length);
    }
}
