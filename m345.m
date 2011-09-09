function b = m345
a= [7 53 183 439 863 497 383 563 79 973 287 63 343 169 583
    627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
    447 283 463 29 23 487 463 993 119 883 327 493 423 159 743
    217 623 3 399 853 407 103 983 89 463 290 516 212 462 350
    960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
    870 456 192 162 593 473 915 45 989 873 823 965 425 329 803
    973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
    322 148 972 962 286 255 941 541 265 323 925 281 601 95 973
    445 721 11 525 473 65 511 164 138 672 18 428 154 448 848
    414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
    184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
    821 461 843 513 17 901 711 993 293 157 274 94 192 156 574
    34 124 4 878 450 476 712 914 838 669 875 299 823 329 699
    815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
    813 883 451 509 615 77 281 613 459 205 380 274 302 35 805];
b = 1000-a;
[row,col] = size(b);
for i=1:row
    b(i,:)=b(i,:)-min(b(i,:));
end
b;
x = min(min(b([2:6,8,9,12:14],[1:3,5:7,10:14])));
b([2:6,8,9,12:14],[1:3,5:7,10:14])=b([2:6,8,9,12:14],[1:3,5:7,10:14])-x;
b(1,[4,8,9,15])=b(1,[4,8,9,15])+x;
b(7,[4,8,9,15])=b(7,[4,8,9,15])+x;
b(10,[4,8,9,15])=b(10,[4,8,9,15])+x;
b(11,[4,8,9,15])=b(11,[4,8,9,15])+x;
b(15,[4,8,9,15])=b(15,[4,8,9,15])+x;
nextx = [1,2,3,5,6,10,11,12,13,14,15];
nexty = [2,3,4,5,6,11,12,13,14];
xs = [4,7,8,9];
ys = [1,7,8,9,10,15];
x = min(min(b(nexty,nextx)));
b(nexty,nextx)=b(nexty,nextx)-x;
for i=1:length(ys)
    b(ys(i),xs)=b(ys(i),xs)+x;
end
nextx = [1:7,10:15];
nexty = [3,4,6,12,13,14];
xs = [8,9];
ys = [1,2,7,8,9,10,15];
x = min(min(b(nexty,nextx)));
b(nexty,nextx)=b(nexty,nextx)-x;
for i=1:length(ys)
    b(ys(i),xs)=b(ys(i),xs)+x;
end
nextx = [1:7,10,11,13:15];
nexty = [3,4,6,10,12,13,14];
xs = [8,9,12];
ys = [1,2,5,7,8,9,15];
x = min(min(b(nexty,nextx)));
b(nexty,nextx)=b(nexty,nextx)-x;
for i=1:length(ys)
    b(ys(i),xs)=b(ys(i),xs)+x;
end
nextx = [1:7,10,11,13:15];
nexty = [3,4,6,10,12,14];
xs = [8,9,12];
ys = [1,2,5,7,8,9,11,13,15];
x = min(min(b(nexty,nextx)));
b(nexty,nextx)=b(nexty,nextx)-x;
for i=1:length(ys)
    b(ys(i),xs)=b(ys(i),xs)+x;
end
nextx = [1:6,10,11,13:15];
nexty = [3,4,6,10,11,12,14];
xs = [7,8,9,12];
ys = [1,2,5,7,8,9,13,15];
x = min(min(b(nexty,nextx)));
b(nexty,nextx)=b(nexty,nextx)-x;
for i=1:length(ys)
    b(ys(i),xs)=b(ys(i),xs)+x;
end
nextx = [1:6,10,11,13:15];
nexty = [3,4,6,10,11,14];
xs = [7,8,9,12];
ys = [1,2,5,7,8,9,12,13,15];
x = min(min(b(nexty,nextx)));
b(nexty,nextx)=b(nexty,nextx)-x;
for i=1:length(ys)
    b(ys(i),xs)=b(ys(i),xs)+x;
end
nextx = [1:6,10,11,13:15];
nexty = [4,6,10,11,14];
xs = [7,8,9,12];
ys = [1,2,3,5,7,8,9,12,13,15];
x = min(min(b(nexty,nextx)));
b(nexty,nextx)=b(nexty,nextx)-x;
for i=1:length(ys)
    b(ys(i),xs)=b(ys(i),xs)+x;
end
nextx = [1:9,11:15];
nexty = [1,3];
xs = [10];
ys = [2,4:15];
x = min(min(b(nexty,nextx)));
b(nexty,nextx)=b(nexty,nextx)-x;
for i=1:length(ys)
    b(ys(i),xs)=b(ys(i),xs)+x;
end
nextx = [1:7,9,11:15];
nexty = [1,3,4];
xs = [8, 10];
ys = [2,5:15];
x = min(min(b(nexty,nextx)));
b(nexty,nextx)=b(nexty,nextx)-x;
for i=1:length(ys)
    b(ys(i),xs)=b(ys(i),xs)+x;
end
nextx = [1:6,8,10,11,13:15];
nexty = [6,10,11,14];
xs = [7,9,12];
ys = [1:5,7,8,9,12,13,15];
x = min(min(b(nexty,nextx)));
b(nexty,nextx)=b(nexty,nextx)-x;
for i=1:length(ys)
    b(ys(i),xs)=b(ys(i),xs)+x;
end
nextx = [2:6,8,10,11,13:15];
nexty = [6,10,11,14];
xs = [1,7,9,12];
ys = [1:5,7,8,9,12,13,15];
x = min(min(b(nexty,nextx)));
b(nexty,nextx)=b(nexty,nextx)-x;
for i=1:length(ys)
    b(ys(i),xs)=b(ys(i),xs)+x;
end
a(1,10)+a(2,11)+a(3,8)+a(4,5)+a(5,4)+a(6,1)+a(7,14)+a(8,3)+a(9,15)+a(10,12)+a(11,7)+a(12,6)+a(13,13)+a(14,9)+a(15,2)
end
