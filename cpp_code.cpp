#include <algorithm>
#include <array>
#include <format>
#include <print>
#include <string>

#ifndef N
#define N 10
#endif


constexpr auto toString(int a){
  std::array<char,29>buf{0};
  bool neg = a < 0 ? [&]() constexpr {
    a = -a;
    return true;
  }() : false;
  int i = 28;
  if(a == 0) {
    buf[0] = '0';
    return std::make_pair(buf, i);
  }
  for(; a && i; --i, a /= 10){
    buf[i] = "0123456789"[a % 10];
  }
  if(neg){
    buf[i] = '-';
    --i;
  }
  std::copy_if(buf.begin(), buf.end(), buf.begin(), [](char woof){
    if(woof == 0) return false;
    return true;
  });
  return std::make_pair(buf, i);
}

template<int i>
constexpr auto doFormat(){
  constexpr std::string_view str{"if(i == ?)"};
  auto start = str.find('?');
  auto [number, a] = toString(i);
  std::array<char, 29> array{0};
  std::copy(str.begin(), str.end(), array.begin());
  auto it = std::copy_if(number.begin(), number.begin() + a, array.begin() + start, [](char woof){
    if(woof == 0) return false;
    return true;
  });
  if(*it != ')')
    *it = ')';
  ++it;
  *it = ' ';
  ++it;
  constexpr std::string_view notEven{"return false;"};
  constexpr std::string_view even{"return true;"};
  if(i & 1) std::copy(notEven.begin(), notEven.end(), it);
  else std::copy(even.begin(), even.end(), it);
  return array;
}



template<int it, int max>
constexpr void make(std::array<std::array<char, 29>, max>& a){
  if constexpr(it == max){
    return;
  }
  else {
    a[it] = doFormat<it>();
    make<it+1, max>(a);
  }
}

template<int i>
constexpr auto meow(){
  std::array<std::array<char, 29>, i+1> aa{std::array<char, 29>{0}};
  make<0, i+1>(aa);
  return aa;
}

int main(){
  constexpr auto i = meow<N>();
  for(const auto& a : i){
    std::println("{}", a.data());
  }
}
