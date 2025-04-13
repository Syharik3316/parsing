import { NextResponse } from "next/server"
import type { NextRequest } from "next/server"

// Пути, которые не требуют аутентификации
const publicPaths = ["/", "/login", "/register", "/features", "/forgot-password"]

export function middleware(request: NextRequest) {
  const userId = request.cookies.get("userId")?.value
  const path = request.nextUrl.pathname

  // Проверка, является ли путь публичным
  const isPublicPath = publicPaths.some((publicPath) => path === publicPath || path.startsWith(`${publicPath}/`))

  // Если путь требует аутентификации, но пользователь не авторизован
  if (!isPublicPath && !userId) {
    const url = new URL("/login", request.url)
    url.searchParams.set("callbackUrl", encodeURI(request.url))
    return NextResponse.redirect(url)
  }

  // Если пользователь авторизован и пытается получить доступ к странице входа или регистрации
  if ((path === "/login" || path === "/register") && userId) {
    return NextResponse.redirect(new URL("/dashboard", request.url))
  }

  return NextResponse.next()
}

export const config = {
  matcher: [
    // Исключаем статические файлы
    "/((?!api|_next/static|_next/image|favicon.ico).*)",
  ],
}
