class App {
  static int largestGap (int [] nums){
    Arrays.sort(nums);

    int result = 0;

    for (int x = 0; x < nums.length-1; x++){
        if (nums[x] == nums[x+1]){
            continue;
        }
        else if (nums[x+1] - nums[x] > result){
            result = nums[x+1] - nums[x];
        }
    }
    return result;
  }
}
