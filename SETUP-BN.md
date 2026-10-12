# GitHub প্রোফাইল সেটআপ

১. ZIP Extract করো। ভেতরের mdabuhanif230 ফোল্ডার খোলো।
২. GitHub-এ Public repository তৈরি করো, নাম ঠিক mdabuhanif230 রাখো। আগে থাকলে সেটাই ব্যবহার করো।
৩. README.md, assets, scripts এবং .github ফোল্ডার repository-র root-এ রাখো। পুরো mdabuhanif230 ফোল্ডারটি আরেকটি সাবফোল্ডার হিসেবে আপলোড করবে না। ZIP ফাইল সরাসরি আপলোড করলে কাজ হবে না।
৪. README আগে থাকলে নতুন README.md দিয়ে সেটি বদলাও; একই সঙ্গে Readme.md নামে পুরোনো ফাইল রাখবে না।
৫. .github ফোল্ডারটি Windows-এ লুকানো থাকতে পারে। Browser upload-এ বাদ পড়লে Git দিয়ে আপলোড করো অথবা GitHub-এ Add file → Create new file থেকে .github/workflows/update-profile.yml তৈরি করে দেওয়া ফাইলের লেখা পেস্ট করো।
৬. Actions → Update profile statistics → Run workflow দিয়ে প্রথমবার চালাও। সফল হলে এরপর প্রতিদিন statistics আপডেট করার চেষ্টা হবে; GitHub schedule কিছুটা দেরিতে চলতে পারে।
৭. Workflow disabled থাকলে Enable করো। লেখার অনুমতির error হলে Settings → Actions → General → Workflow permissions পরীক্ষা করো। Branch protection থাকলে bot-এর push বাধা পেতে পারে।

## Windows CMD দিয়ে Git আপলোড

নতুন/খালি repository-র জন্য, Extract করা mdabuhanif230 ফোল্ডারে CMD খুলে:

```bat
git init
git add .
git commit -m "Add personalized GitHub profile"
git branch -M main
git remote add origin https://github.com/mdabuhanif230/mdabuhanif230.git
git push -u origin main
```

আগে repository-তে ফাইল থাকলে সেটি clone করে এই ZIP-এর ফাইলগুলো সেখানে কপি করো, তারপর git add ., git commit এবং git push করো। Force push প্রয়োজন নেই। GitHub-এ লগইন/অনুমতি চাইলে নিজের অ্যাকাউন্ট দিয়ে সম্পন্ন করো।

## কী আপডেট হয়

- তোমার নাম, skill, email ও project links আগে থেকেই বসানো আছে। এগুলো বদলাতে README.md এবং প্রয়োজনমতো assets-এর SVG সম্পাদনা করতে হবে।
- Public repository সংখ্যা, followers, original repositories-এর stars ও প্রধান language-এর repository count স্বয়ংক্রিয়ভাবে আপডেট হয়। কোনো personal access token বা নতুন secret লাগবে না; workflow GitHub-এর নিজস্ব token ব্যবহার করে।
- Semester দেওয়া হয়নি, তাই নির্দিষ্ট semester লেখা নেই। চাকরির অভিজ্ঞতা ও portfolio দেওয়া হয়নি, তাই দাবি বা খালি লিংক নেই।
- WhatsApp username-এর নির্ভরযোগ্য direct link দেওয়া হয়নি, তাই বাটন নেই। পরে shareable WhatsApp link দিলে যুক্ত করা যাবে।
- Banner ও skills স্থানীয় SVG। Typing animation বাইরের service থেকে আসে; service বন্ধ থাকলেও মূল প্রোফাইল দেখা যাবে। SVG animation বন্ধ থাকলে স্থির ডিজাইন দেখা যাবে।
- এই ZIP-এ কারও পুরোনো statistics, achievements বা personal contact কপি করা হয়নি।

Official references:
https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme
https://docs.github.com/en/actions/tutorials/authenticate-with-github_token
