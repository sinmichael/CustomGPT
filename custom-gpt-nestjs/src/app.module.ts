import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { RedisService } from './redis/redis.service';

@Module({
  controllers: [AppController],
  providers: [AppService, RedisService],
})
export class AppModule {}
