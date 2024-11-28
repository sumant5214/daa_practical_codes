import java.math.BigInteger;

class BigInt {
    BigInteger karatsuba(BigInteger X, BigInteger Y) {
        if (X.compareTo(BigInteger.TEN) < 0 && Y.compareTo(BigInteger.TEN) < 0) {
            return X.multiply(Y);
        }
        int maxSize = Math.max(getSize(X), getSize(Y));
        if (maxSize < 10) {
            return X.multiply(Y);
        }
        int halfSize = (maxSize + 1) / 2;
        BigInteger power = BigInteger.TEN.pow(halfSize);
        BigInteger a = X.divide(power);

        BigInteger b = X.remainder(power);
        BigInteger c = Y.divide(power);
        BigInteger d = Y.remainder(power);
        BigInteger ac = karatsuba(a, c);
        BigInteger bd = karatsuba(b, d);
        BigInteger abcd = karatsuba(a.add(b), c.add(d));
        return ac.multiply(power.pow(2)).add(
                abcd.subtract(ac).subtract(bd).multiply(power)).add(bd);
    }

    private int getSize(BigInteger num) {
        return num.toString().length();
    }

    public static void main(String[] args) {
        BigInt bigInt = new BigInt();
        BigInteger num1 = new BigInteger("5678");
        BigInteger num2 = new BigInteger("1234");
        BigInteger result = bigInt.karatsuba(num1, num2);
        System.out.println("Karatsuba result: " + result);
        System.out.println("Built-in multiplication result: " + num1.multiply(num2));
    }
}