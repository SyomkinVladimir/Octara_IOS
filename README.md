# Octara iOS

Новый iOS-проект VPN-клиента для iPhone.

## Цель
Сделать отдельное приложение с нуля, используя только полезные идеи из macOS-версии.

## Приоритет
Первая версия = один рабочий split-режим.

## Структура
- `docs/` — документация проекта
- `shared/` — общая логика
- `app/` — интерфейс приложения
- `ios_native/` — нативная iOS VPN-часть

## Architecture note

The `shared/` Python code is a reference implementation and test layer for profile parsing and configuration logic.

It is not intended to run inside the iOS Network Extension.

Planned roles:
- `shared/` — reference logic, parsing, validation, tests
- `app/` — application layer and UI-facing code
- `ios_native/` — future native iOS/Swift/Go integration for VPN runtime
