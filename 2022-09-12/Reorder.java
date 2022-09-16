class Reorder {
    static int [] reorderDigits (int [] digits, String order){
        if (order.equals("asc")){
            Arrays.sort(digits);
            return digits;
        }
        else{ //(order.equals("desc")){
            Arrays.sort(digits);
            int ret [] = new int [digits.length];
            for (int x = 0; x < digits.length; x++){
                ret[ret.length-1-x] = digits[x];
            }
            return ret;
        }
    }
}
